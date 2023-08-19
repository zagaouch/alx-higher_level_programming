#include <Python.h>
#include <stdio.h>
/**
 * print_python_list - python liste
 * @p : pointer
*/
void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *item;

    if (!PyList_Check(p))
    {
        printf("[ERROR] Invalid Python List\n");
        return;
    }

    size = PyList_Size(p);

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);

    printf("[*] Elements: ");
    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("%s", Py_TYPE(item)->tp_name);
        if (i < size - 1)
            printf(", ");
    }
    printf("\n");
}
/**
 * print_python_bytes - python liste
 * @p : pointer
*/
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    char *bytes;

    if (!PyBytes_Check(p))
    {
        printf("[ERROR] Invalid Python Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);

    printf("[.] Python bytes info\n");
    printf("  [.] Size of the Python Bytes Object: %ld\n", size);
    printf("  [.] Bytes: ");

    bytes = PyBytes_AsString(p);

    if (size > 10)
        size = 10;

    for (i = 0; i < size; i++)
    {
        printf("%02x", (unsigned char)bytes[i]);
        if (i < size - 1)
            printf(" ");
    }
    printf("\n");
}