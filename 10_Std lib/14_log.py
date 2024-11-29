### 로깅 ###

# 로깅 레벨의 의미
# DEBUG : 전혀 이상이 없지만, 임의의 순간에서 정보를 확인하려는 목적(개발자 마음)
# INFO : 전혀 이상이 없지만, 중요한 이벤트가 달성 되었는지 확인하려는 목적(빈도↓)
# WARNING : 예상 가능한 수준에서 문제가 발생했다는 경고 목적
# ERROR : 예상하지 못한 문제가 발생
# CRITICAL : 예상하지 못한 문제가 발생(심각), ERROR와 차별하기 위한.

# 빈도 DEBUG > INFO > WARNING > ERROR > CRITICAL
# 예시> 출력레벨=WARNING, (WARNING, ERROR, CRITICAL만 보여줌)
import logging
logging.basicConfig(level=logging.DEBUG)  # 기본 로깅 수준을 DEBUG로 설정

logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')