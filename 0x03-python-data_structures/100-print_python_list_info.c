#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *py_list)
{
    long int list_size = PyList_Size(py_list);
    int i;
    PyListObject *list_obj = (PyListObject *)py_list;

    printf("[*] Size of the Python List = %li\n", list_size);
    printf("[*] Allocated memory = %li\n", list_obj->allocated);
    
    for (i = 0; i < list_size; i++) {
        PyObject *element = list_obj->ob_item[i];
        printf("Element %i: %s (Address: %p)\n", i, Py_TYPE(element)->tp_name, element);
    }
}

