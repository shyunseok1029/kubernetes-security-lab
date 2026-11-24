# Kubernetes Security Lab

Kubernetes와 웹 애플리케이션 보안을 학습하며 구현하고 검증한 내용을 정리한 개인 프로젝트입니다. 사후에 작성한 보안 구현과 개인 인프라 실습 기록을 구분해 소개합니다.

## Security Implementation

- [Flask 파일 압축 기능 및 입력값 검증](safe_report_archive.py): 서버의 허용 목록으로 파일을 선택하고 Python `zipfile`로 압축합니다. 셸을 사용하지 않으며 파일 접근 오류에 일반적인 응답을 반환합니다.
- [ServiceAccount 토큰 자동 마운트 제어](serviceaccount-example.yaml): API 접근이 필요 없는 가상 웹앱에서 토큰 자동 마운트를 비활성화합니다.
- [Kubernetes RBAC 최소 권한 설계](rbac-minimal.yaml): 가상의 `demo` Namespace에서 지정된 ConfigMap 한 개에 `get`만 허용합니다. 토큰 마운트와 RBAC 인가는 별개의 설정입니다.

이 구현은 개인 학습을 위해 사후에 새로 작성한 것으로, 팀 프로젝트 당시의 코드나 설정이 아닙니다. Flask 구현에는 Flask와 서버가 관리하는 가상 보고서 파일이 별도로 필요합니다.

## Kubernetes Infrastructure Practice

- [Minikube / RBAC](docs/minikube-rbac.md): 기본 리소스 구성과 ServiceAccount 권한 조회
- [VMware 멀티노드 Kubernetes](docs/vmware-multinode.md): kubeadm, containerd, Calico와 노드·시스템 Pod 상태 확인
- [Helm](docs/helm-practice.md): Chart 설치, Upgrade, Revision 확인 및 Rollback
- [Argo CD](docs/argocd-practice.md): 공개 애플리케이션의 Manual Sync와 재동기화

## 검증 범위

- **Flask:** 임시 파일과 테스트 클라이언트로 정상 ZIP 생성, 잘못된 입력과 경로 조작 거부, 누락 파일 응답을 확인했습니다. 접근 오류는 모의 예외로 시험했으며, 셸과 외부 프로세스 호출을 차단했습니다.
- **ServiceAccount / RBAC:** YAML 구문과 권한 관계를 정적으로 확인했습니다. 이 저장소의 설정은 클러스터에 적용하지 않았습니다.
- **인프라 실습:** 별도의 개인 실습 기록과 기존 조사에서 확인된 범위만 각 문서에 정리했습니다. Pod 생성 거부와 Argo CD Drift의 중간 상태는 증빙이 부분적입니다.

## 향후 학습

격리된 개인 Kubernetes 환경에서 ServiceAccount와 RBAC 동작을 검증하고 학습 기록을 확장할 계획입니다.
