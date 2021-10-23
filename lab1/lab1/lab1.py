import sys
import math

def get_coef(index, prompt):
    try:
        coef_str = sys.argv[index]
        coef = float(coef_str)
    except:
        while True:
            print(prompt)
            coef_str = input()
            try:
                coef = float(coef_str)
                break
            except:
                print('попробуй еще раз')
    return coef



def get_roots(a, b, c, result):
    if a == 0 and b == 0:
        if c == 0:
            return -1
    elif a == 0 and b != 0:
        tmp = -c / b
        try:
            tmp = math.sqrt(tmp)
            result.add(-tmp)
            result.add(tmp)
        except: pass
    else:
        D = b * b - 4 * a * c
        if D > 0:
            D = math.sqrt(D)
            try:
                tmp = math.sqrt((-b - D) / 2 * a)
                result.add(-tmp)
                result.add(tmp)
            except: pass
            try:
                tmp2 = math.sqrt((-b + D) / 2 * a)
                result.add(-tmp2)
                result.add(tmp2)
            except: pass
        elif D == 0:
            try:
                tmp = math.sqrt(-b / 2 * a)
                result.add(-tmp)
                result.add(tmp)
            except: pass
    return len(result)

def main():
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    
    roots = set()
    len_roots = get_roots(a, b, c, roots)

    if len_roots == -1:
        print('Корней бесконечное множество')
    elif len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: ', roots)
    elif len_roots == 2:
        print('Два корня: ', roots)
    elif len_roots == 3:
        print('Три корня: ', roots)
    elif len_roots == 4:
        print('Четыре корня: ', roots)

# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()
