# Minikube와 RBAC 개인 실습

## 목적과 환경

개인 로컬 Minikube 환경에서 Kubernetes의 기본 리소스를 구성하고, ServiceAccount와 RBAC를 통해 워크로드의 권한 범위를 살펴본 실습입니다. WHS 팀 프로젝트와는 별개의 개인 활동입니다.

## 수행 내용과 확인 결과

기존 개인 실습 조사 기록에는 다음 작업과 결과가 연결되어 있습니다.

- Namespace를 구분하고 Workload와 Service를 구성한 뒤 리소스 상태와 HTTP 응답을 확인했습니다.
- ServiceAccount, Role, RoleBinding을 구성하고 권한 조회를 실습했습니다.
- 권한 조회 기록에서 Pod 조회 허용 결과를 확인했습니다.

Pod 생성 거부 결과는 캡처 일부가 잘려 있어 완전한 검증 결과로 주장하지 않습니다. 정확한 정책 내용, 명령과 원본 화면의 공개 범위도 별도 확인이 필요합니다.

## 이해한 개념

Namespace는 리소스를 구분하는 범위입니다. ServiceAccount는 워크로드가 Kubernetes API에 접근할 때 사용할 수 있는 주체이며, Role은 Namespace 내에서 허용할 리소스와 동작을 정의합니다. RoleBinding은 해당 Role을 주체에 연결합니다. 토큰이 마운트되는지와 API 요청이 인가되는지는 별개의 문제입니다.

## 근거와 한계

개인 실행 흔적, PDF 캡처와 로컬 상태 기록을 정리한 기존 조사 문서를 근거로 합니다. 이 문서에는 원본 캡처, Secret, 계정과 환경 식별자를 포함하지 않았으며 이번에 실습을 다시 실행하지 않았습니다. 원본 공개 여부와 정확한 개별 권한은 추가 확인이 필요합니다.

별도로 새로 작성한 [ServiceAccount](../serviceaccount-example.yaml)와 [최소 권한 RBAC](../rbac-minimal.yaml) 설정은 당시 사용한 설정의 복사본이 아닙니다.
