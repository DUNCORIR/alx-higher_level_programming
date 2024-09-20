#include <Python.h>
#include <stdio.h>
/**
 * print_python_list - Print information about a Python list.
 * @p: Pointer to the Python list object.
 */
void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		printf("Error: Invalid List Object\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %zd\n", size);

	printf("[*] Allocated = %zd\n", allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);

		printf("Element %zd: %s\n", i, item->ob_type->tp_name);
		if (PyBytes_Check(item))
		{
			print_python_bytes(item);
		}
	}
}

#include <Python.h>
#include <stdio.h>
/**
 * print_python_bytes - Print information about a Python bytes object.
 * @p: Pointer to the Python bytes object.
 */
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		printf("Error: Invalid Bytes Object\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);
	char *bytes_content = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  size: %zd\n", size);
	printf("  trying string: %.*s\n", (int)size, bytes_content);
	printf("  first %zd bytes: ", size < 10 ? size : 10);

	for  (Py_ssize_t i = 0; i < (size < 10 ? size : 10); i++)
	{
		printf("%02x ", (unsigned char)bytes_content[i]);
	}
	printf("\n");
}
