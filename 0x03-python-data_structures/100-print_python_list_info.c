#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
* print_python_list_info - prints info about python list
* @p: python object
**/

void print_python_list_info(PyObject *p)
{
	long int Size = PyList_Size(p);
	int i;
	PyListObject *object = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", Size);
	printf("[*] Allocated = %li\n", object->allocated);
	for (i = 0; i < Size; i++)
		printf("Element %i: %s\n", i, Py_TYPE(object->ob_item[i])->tp_name);
}
