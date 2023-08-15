#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
/**
 * print_python_list_info - printputhon list info
 * @p: list puthon
*/
void print_python_list_info(PyObject *p)
{
    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t i;

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        PyObject *item = PyList_GetItem(p, i);
        const char *typeName = Py_TYPE(item)->tp_name;

        printf("Element %ld: %s\n", i, typeName);
    }
}
