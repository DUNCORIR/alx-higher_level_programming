#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Function prints basic info
 * about python lists.
 * @p: Is a pointer to the python list.
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size;
	Py_ssize_t alloc, i;
	PyObject *item;

	if (!PyList_Check(p)) /* check if p is a valid list */
		return;

	size = PyList_Size(p); /* Get size and allocated memory */
	alloc = ((PyListObject *)p)->allocated;

	/* print sizes and allocated space */
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", alloc);

	/* Loop thro list then print each element's type */
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
