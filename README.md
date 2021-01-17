# makeSpringMvcFileAuto
회사에서 spring 프레임워크로 개발하고 있는 rest api 서버 애플리케이션은 api 도메인 별로 매번 같은 구조의 파일을 만들어야 합니다.   (controller, service, repository, model, vo, mapper) 그래서 초기 작업 생산성을 높이고자 json 형식으로 만들고자 하는 도메인 이름 및 함수들의 request, response parameter를 정의해주면, 자동으로 파일과 폴더들을 만들어주는 자동화? 프로그램을 만들기로 했습니다.
