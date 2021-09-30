# logger

### 1.logger_proxy

- logger 通常定义为全局变量，利用代理模式，实现logger的延迟绑定，避免logging配置不生效
- demo
 
```
from logger.logger_proxy import LoggerProxy

logger: LoggerProxy = LoggerProxy(__name__)


logger.info("...")
```
