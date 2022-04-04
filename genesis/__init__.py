from decimal import FloatOperation, getcontext, setcontext

DEFAULT_DECIMAL_CONTEXT = getcontext()
DEFAULT_DECIMAL_CONTEXT.prec = 30
DEFAULT_DECIMAL_CONTEXT.traps[FloatOperation] = True
setcontext(DEFAULT_DECIMAL_CONTEXT)
