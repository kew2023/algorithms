# Восходящий подход
# Функция для поиска наиболее эффективного способа умножения
# заданная последовательность матриц
def matrixChainMultiplication(dims):
    n = len(dims) #Кол-во операций
    # c[i, j] = минимальное количество скалярных умножений (т. е. стоимость) для матрица A[i]*..*A[j]
    # Стоимость равна нулю при умножении одной матрицы
    c = [[0 for x in range(n + 1)] for y in range((n + 1))] #Создание матрицы стоимостей
    for length in range(2, n + 1):        # Длина подпоследовательности
        for i in range(1, n - length + 2): #Начало последовательности
            j = i + length - 1 #Конец последовательности
            c[i][j] = float('inf') #Изначально стоимости с A[i] по A[j] максимальна (для дальнейшего уменьшения)
            
            k = i # Итерация в последовательности
            while j < n and k <= j - 1:
                cost = c[i][k] + c[k + 1][j] + dims[i - 1] * dims[k] * dims[j]
                #cost= <i по k> + <k+1 по j> + <k-ая матрица>
                #if cost < c[i][j]: # Проверка новой стоимости
                c[i][j] = cost 
                k = k + 1 #Сдвиг
    return c[1][n - 1],c

dims = [100, 100, 5, 50, 10]
#print('The minimum cost is', matrixChainMultiplication(dims)[0])

#print(*matrixChainMultiplication(dims)[1],sep = '\n')
arr = matrixChainMultiplication(dims)[1]
newarr = matrixChainMultiplication(dims)[1]

for i in range(1,len(arr)-1):
    for j in range(i+1,len(arr[i])-1):
        if i == 1:
            newarr[i][j] = arr[1][len(arr)-2] #Если первая скобка в начале
        else:
            if i == j:
                newarr[i][j] = arr[1][len(arr)-2] #Если в скобках одно число
            elif j == len(arr[i])-2: 
                newarr[i][j] += arr[1][i-1] + dims[0]*dims[i-1]*dims[j] #Если несколько чисел в скобках
            else: 
                newarr[i][j] += arr[1][i-1] + arr[j+1][len(dims)-1] + dims[0]*dims[i-1]*dims[j] + dims[0]*dims[j]*dims[-1]

print()
#print(*newarr,sep = '\n')
print()
clear = []
k = -1
for i in range(1,len(newarr)-1):
    clear += [[]]
    k += 1
    for j in range(1,len(newarr[i])-1):
        clear[k] += [newarr[i][j]]
print(*clear,sep='\n')
minc = float('inf')
for i in range(len(clear)):
    for j in range(len(clear[i])):
        if clear[i][j] != 0 : minc = min(minc, clear[i][j]) 
print(f'min is {minc}')
