#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#define OK 0
#define ERROR 1
#define ZERO_DEF -1

void clean_buf()
{
    char a = getchar();
    while (a != '\n' && a != EOF)
        a = getchar();
}

void free_mat(long double ***arr, int n) {
    for (int i = 0; i < n; i++)
        free((*arr)[i]);
    free(*arr);
}

long double **create_mat(int n, int *err) {
    *err = OK;
    long double **arr = calloc(n, sizeof(long double *));
    if (arr == NULL) {
        *err = ERROR;
    } else {
        for (int i = 0; i < n && *err == OK; i++) {
            arr[i] = calloc(n, sizeof(long double));
            if (arr[i] == NULL) {
                *err = ERROR;
                free_mat(&arr, i);
            }
        }
    }
    if (*err == ERROR)
        printf("Проблемы с выделением памяти, Босс(\n");
    return arr;
}

int read_int(char str[]) {
    printf("%s", str);
    int flag = 1;
    int n;
    while (flag) {
        if (scanf("%d", &n) != 1 || n < 0)
        {
            printf("Ошибка ввода! Повторите попытку ввода целого неотрицательного числа: ");
        } else {
            flag = 0;
        }
        clean_buf();
    }
    return n + 1;
}

long double read_double(char str[]) {
    printf("%s", str);
    long double n;
    while (scanf("%Lf", &n) != 1)
    {
        clean_buf();
        printf("Ошибка ввода! Повторите попытку ввода вещественного числа: ");
    }
    clean_buf();
    //printf("%Lf\n", n);
    return n;
}

void print_matrix(long double **mat, int size) {
    printf("Матрица:\n");
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++)
            printf("%.15Lf ", mat[i][j]);
        printf("\n");
    }
    if (size == 0)
        printf("Матрица пуста.");
    printf("\n");
}

void print_array(long double arr[], int size) {
    printf("Массив:\n");
    for (int i = 0; i < size; i++)
        printf("%.15Lf\n", arr[i]);
    if (size == 0)
        printf("Массив пуст.");
    printf("\n");
}

void print_res(long double arr[], int n) {
    if (n - 1 < 0)
        printf("Результат:\n P0(x) =");
    else
        printf("Результат:\n P%d(x) = ", n - 1);
    for (int i = 0; i < n; i++) {
        char *plus = "+ ";
        if (i == 0 || arr[n - i - 1] < 0)
            plus = "";
        if (i < (n - 1))
            printf("%s%.2Lf * x^%d ", plus, arr[n - i - 1], n - i - 1);
        else
            printf("%s%.2Lf ", plus, arr[n - i - 1]);
    }
    if (n == 0)
        printf("0");
    printf("\n");
}

int input_all(long double ***arr, long double **yrr, int *err) {
    *err = OK;
    int n = read_int("Введите степень уравнения: ");
    int count_diff = read_int("Введите известное количество производных: ");
    int count_points = ceil(((double) n) / ((double) count_diff));
    *arr = create_mat(n, err);
    if (*err == OK) {
        *yrr = calloc(n, sizeof(long double));
        if (*yrr == NULL) {
            free_mat(arr, n);
            *err = ERROR;
        } else {
            for (int j = 0; j < count_points; j++) {
                char message[50];
                long double xi;
                int *diff_arr = calloc(n, sizeof(int));
                if (diff_arr == NULL) {
                    free_mat(arr, n);
                    free(*yrr);
                    *err = ERROR;
                } else {
                    for (int k = 0; k < n; k++)
                        diff_arr[k] = 1;
                    sprintf(message, "Введите x%d : ", j + 1);
                    xi = read_double(message);
                    for (int l = 0; l < count_diff; l++)
                        for (int m = l; m < n; m++) {
                            if ((l + j * count_diff) < n)
                                (*arr)[l + j * count_diff][m] = powl(xi, (m - l)) * diff_arr[m];
                            diff_arr[m] *= m - l;
                        }
                    sprintf(message, "Введите y%d : ", j + 1);
                    (*yrr)[j * count_diff] = read_double(message);
                    //printf("TYT!\n\n");
                    for (int l = 1; l < count_diff; l++)
                        if ((l + j * count_diff) < n) {
                            sprintf(message, "Введите производную №%d : ", l);
                            (*yrr)[l + j * count_diff] = read_double(message);
                        }
                }
            }
        }
    }
    return n;
}

long double **make_minor(long double **arr, int n, int i, int *err) {
    *err = OK;
    long double **minor = create_mat(n - 1, err);
    if (*err == OK) {
        for (int row = 1; row < n; row++)
            for (int col = 0; col < n; col++)
                if (col != i)
                    minor[row - 1][col - (col > i)] = arr[row][col];
    }
    return minor;
}

long double calc_def(long double **arr, int n, int *err) {
    *err = OK;
    if (n <= 0)
        return 0;
    if (n == 1)
        return arr[0][0];
    if (n == 2)
        return arr[0][0] * arr[1][1] - arr[1][0] * arr[0][1];
    long double res = 0;
    for (int i = 0; i < n && *err == OK; i++) {
        long double **minor = make_minor(arr, n, i, err);
        if (*err == OK) {
            res += arr[0][i] * calc_def(minor, n - 1, err) * powl(-1, i);
            if (*err == OK)
                free_mat(&minor, n - 1);
        }
    }
    return res;
}

long double calc_ai(long double **arr, long double *yrr, int n, int ind, long double def_main, int *err) {
    *err = OK;
    long double def_ai = 0;
    long double **arr_new = create_mat(n, err);
    if (*err == OK) {
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                arr_new[i][j] = arr[i][j];
        for (int i = 0; i < n; i++)
            arr_new[i][ind] = yrr[i];
        def_ai = calc_def(arr_new, n, err);
        if (*err == OK)
            free_mat(&arr_new, n);
    }
    return def_ai / def_main;
}

int main(void) {
    int rc = OK;
    long double **arr;
    long double *yrr;
    int n = input_all(&arr, &yrr, &rc);
    if (rc == OK) {
        long double def_main = calc_def(arr, n, &rc);
        if (rc == OK) {
            if (def_main == 0) {
                printf("Система уравнений не имеет единственного решения, так как определитель матрицы равен 0.\n\
        Возможно, система имеет бесконечно много решений или не имеет решений вовсе.");
                rc = ZERO_DEF;
            } else {
                long double *res_a = calloc(n, sizeof(long double));
                if (res_a == NULL)
                    rc = ERROR;
                else {
                    for (int i = 0; i < n && rc == OK; i++) {
                        long double ai = calc_ai(arr, yrr, n, i, def_main, &rc);
                        if (rc == OK)
                            res_a[i] = ai;
                    }
                    if (rc == OK)
                        print_res(res_a, n);
                    free(res_a);
                }
            }
        }
        free_mat(&arr, n);
        free(yrr);
    }
    return rc;
}
