"""독립적인 개인 학습용 Flask 예제.

WHS 팀 프로젝트의 원본 코드가 아니며, 서버가 관리하는 허용 목록의
파일만 Python 표준 라이브러리로 압축하는 안전한 처리 흐름을 보여준다.
"""

from __future__ import annotations

import io
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from flask import Flask, abort, request, send_file


app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent
REPORT_DIR = BASE_DIR / "demo_reports"

# 사용자 입력으로 경로를 만들지 않고, 서버가 미리 정한 항목만 선택한다.
ALLOWED_REPORTS = {
    "summary": REPORT_DIR / "summary.txt",
    "findings": REPORT_DIR / "findings.txt",
}


def resolve_allowed_report(report_key: str) -> Path:
    """허용 목록과 기준 디렉터리를 모두 확인한 뒤 파일을 반환한다."""

    candidate = ALLOWED_REPORTS.get(report_key)
    if candidate is None:
        abort(400, description="unknown report")

    try:
        resolved = candidate.resolve(strict=True)
        report_root = REPORT_DIR.resolve()
    except FileNotFoundError:
        abort(404, description="report not found")
    except OSError:
        abort(503, description="report temporarily unavailable")

    if report_root not in resolved.parents:
        abort(400, description="report is outside the allowed directory")

    return resolved


@app.get("/archive")
def archive_report():
    """허용된 단일 보고서를 메모리에서 ZIP으로 만들어 반환한다."""

    report_key = request.args.get("report", "summary")
    report_path = resolve_allowed_report(report_key)

    archive_data = io.BytesIO()
    try:
        with ZipFile(archive_data, mode="w", compression=ZIP_DEFLATED) as archive:
            archive.write(report_path, arcname=report_path.name)
    except FileNotFoundError:
        abort(404, description="report not found")
    except OSError:
        abort(503, description="report temporarily unavailable")

    archive_data.seek(0)
    return send_file(
        archive_data,
        mimetype="application/zip",
        as_attachment=True,
        download_name=f"{report_key}.zip",
    )
