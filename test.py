class A:
	def _foo(self):
		print('foo')

a = A()

foo = getattr(a, '_foo')
foo()