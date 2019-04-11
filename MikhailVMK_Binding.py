class ForwardFunction:
	def __init__(self, *args, handler, method):
		self._args = args
		self._forwardFunction = getattr(handler, method)
	def __call__(self, event):
		self._forwardFunction(*self._args, event)
		
