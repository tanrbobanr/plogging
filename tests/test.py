"""Code used to test the module.

"""
import sys
sys.path.append(".")
from src import plogging

# default formatter
log = plogging.setup_new("logger", level=10, package="test")

log.debug("debug")
log.info("info")
log.warning("warning")
log.error("error")
log.critical("critical")

del log

# custom formatter
fmt = ("NAME[{name}]; MESSAGE[{message}]; ARGS[{args}]; LEVELNAME[{levelname}]; LEVELNO[{levelno}];"
       " PATHNAME[{pathname}]; FILENAME[{filename}]; MODULE[{module}]; EXC_INFO[{exc_info}]; "
       "EXC_TEXT[{exc_text}]; STACK_INFO[{stack_info}]; LINENO[{lineno}]; FUNCNAME[{funcName}]; "
       "CREATED[{created}]; MSECS[{msecs}]; RELATIVECREATED[{relativeCreated}]; THREAD[{thread}]; "
       "THREADNAME[{threadName}]; {enter}PROCESSNAME[{processName}]{exit}; PROCESS[{process}]; "
       "ASCTIME[{_asctime}]; DEFAULT[{default}]")

palette = plogging.Palette(
    plogging.LevelContainer(
        "32;1",
        "34;1",
        "33;1",
        "31;1",
        "41"
    )
)
formatter = plogging.Formatter(
    fmts=plogging.LevelContainer(
        "DEBUG: " + fmt,
        "INFO: " + fmt,
        "WARNING: " + fmt,
        "ERROR: " + fmt,
        "CRITICAL: " + fmt
    ),
    datefmt="%Y-%m-%d %H:%M:%S",
    defaults={"default": "default_value"},
    backup_fmts=plogging.LevelContainer(
        "DEBUG: " + fmt,
        "INFO: " + fmt,
        "WARNING: " + fmt,
        "ERROR: " + fmt,
        "CRITICAL: " + fmt
    ),
    name=palette,
    message=palette,
    args=palette,
    levelname=palette,
    levelno=palette,
    pathname=palette,
    filename=palette,
    module=palette,
    exc_info=palette,
    exc_text=palette,
    stack_info=palette,
    lineno=palette,
    funcName=palette,
    created=palette,
    msecs=palette,
    relativeCreated=palette,
    thread=palette,
    threadName=palette,
    processName=palette,
    process=palette,
    # asctime=palette,
    default=palette
)


log = plogging.setup_new("logger", level=10, formatter=formatter, package="test.custom")

log.debug("debug")
log.info("info")
log.warning("warning")
log.error("error")
log.critical("critical")


