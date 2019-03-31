package lesson2;

import java.util.Comparator;
import java.util.Iterator;

/*
class List<Item>implments Interable<Item>
АТД "Список" должен содержать методы:
1) void add(Item item)
2) boolean remove(Item item)
3) Item get(int index)
4) void set(int index, Item item)
5) int indexOf(Item item)
6) boolean contains(Item item)
7) int size()
*/
public class AbstractDataTypeList<Item> implements Iterable<Item>{
    private Object[] list = new Object[1]; //Массив из одного элемента, так как мы сможем изменять длину массива
    private int size = 0; //Переменная количества элементов в списке

    //Метод возвращающий колиичество элементов в списке
    public int size() {
        return size;}

    //Метод полученя элемента массива по его номеру. Аналог - //arr[index]
    public Item get(int index) {
        if (index < 0 || index > size - 1) {
            throw new IndexOutOfBoundsException(); //Ошибка, если индекс меньше нуля или меньше количества элементов в массиве
        }
        return (Item) list[index]; //Приведение типов к Item. Но ошибка, "Непроверенное приведение типов"
    }

    //Передаем номер элемента который хотим изменить и значение которое хотим в него записать.
    //Аналог - arr[index] = item
    public void set(int index, Item item) {
        if (index < 0 || index > size - 1) {
            throw new IndexOutOfBoundsException(); //Ошибка, если индекс меньше нуля или меньше количества элементов в массиве
        }
        list[index] = item;
    }

    //Метод ничего не возвращает, а в качестве параметра принимает новую вместимость массива
    private void resize(int capacity) {
        Object[] temp = new Object[capacity]; //Вспомогательный массив

        for (int i = 0; i < list.length; i++) {
            temp[i] = list[i];
        }
        list = temp;
        //У объекта list меняем ссылку на новый вспомогательный массив с измененным объемом.
        //Ссылка на старый массив и сам старый массив будут удалены сборщиком мусора
    }

    //Если мы пытаемся добавить элемент, но для него места в массиве не достаточно, то увеличиваем размер массива
    public void add(Item item) {
        if (size == list.length) {
            resize(2 * list.length); //Вспомогательный метод. Увеличиваем размер массива в два раза
        }
        list[size] = item; //Добавляем новый элемент в массив
        size++; //Уведичиваем переменную количеста элементов в массиве на единицу
    }

    //Удаляем элемент массива путем перекрытия его соседним. В итоге последний заменяем на null. Возвращает значечние: удалили мы элемент или нет.
    public boolean remove(Item item) {
        int index = indexOf(item);
        if (index == -1) { //Метод indexOf вернул -1, значит элемент не найден
            return false;
        }
        for (int i = index; i < size - 1; i++) {
            list[i] = list[i + 1];
        }
        list[size - 1] = null; //Последнему элементу присваиваем null, так как там ранее был элемент, но он сдвинулся влево и его нужно затереть
        size--;
        if (size == list.length / 4 && size > 0) { //Уменьшаем массив в два раза, если он заполнен на 1/4
            resize(list.length / 2);
        }
        return true;
    }

    //Ищем элемент в массиве с помощью линейного поиска. Если не нашли, то возвращаем -1, если нашли, то возвращаем его
    public int indexOf(Item item) {
        for (int i = 0; i < size; i++) {
            if (list[i].equals(item)) {
                return i;
            }
        }
        return -1;
    }

    //Метод, который говорит нам существует ли элемент. Возвращает да/нет
    public boolean contains(Item item) {
        return indexOf(item) > -1;
    }

    //Скрытый внутренний объект класса, который реализовывает интерфейс итератор.
    private class AbstractDataTypeListIterator implements Iterator<Item> {

        private int cursor = 0;//Переменная - курсор (указатель на текущий элемент)

        //Метод возвращающий ответ на вопрос: Есть ли следующий элемент?
        @Override
        public boolean hasNext() {
            return cursor != size;
        }

        //Метод возвращает очередной элемент в списке. Всегда перед вызовом метода next должен быть вызов метода hasNext
        @Override
        public Item next() {
            if (!hasNext()) {
                throw new IndexOutOfBoundsException();
            }
            Item item = (Item) list[cursor];//Вспомогательная переменная в которой хранится переменная, которую будем двигать
            cursor++; //Передвигаем курсор
            return item;
        }
    }

    //Обязательный метод перебираемного списка
    @Override
    public Iterator<Item> iterator() {
        return new AbstractDataTypeListIterator();
    }

    //Метод возвращающий массив в виде строки
    @Override
    public String toString() {
        StringBuilder str = new StringBuilder();
        for (int i = 0; i < size; i++) {
            str.append(list[i].toString() + ", ");
        }
        return str.toString();
    }

    //Метод меняющий местами два элемента
    private void exch(int x, int y) {
        Object temp = list[x];
        list[x] = list[y];
        list[y] = temp;
    }

    //Метод возвращающий знаечние да/нет. Меньше ли первый объект, чем второй.
    //Comparator<Item> cmp - компоратор (сравниватель) элементов Item
    private boolean less(Item item1, Item item2, Comparator<Item> cmp) {
        return cmp.compare(item1, item2) < 0;
    }

    //Сортировка выбором. Реализация с помощью компоратора
    public void selectionSort(Comparator<Item> cmp) {
        for (int i = 0; i < size - 1; i++) { //Идем от первого элемента до предпоследнего, так как последний и так окажется на своем месте
            int min = i;
            for (int j = i + 1; j < size; j++) {
                if (less((Item) list[j], (Item) list[min], cmp)) {
                    min = j; //Если нашелся элемент, меньше текущего минимального, то переопределяем его
                }
            }
            exch(i, min); //Обмениваем текущий элемент с минимальным
        }
    }

    //Сортировка вставками. Реализация с помощью компоратора
    public void insertionSort(Comparator<Item> cmp) {
        for (int i = 0; i < size; i++) {
            for (int j = i; j > 0; j--) {
                if (less((Item) list[j], (Item) list[j - 1], cmp)) {
                    exch(j, j - 1);
                }
                else {
                    break;
                }
            }
        }
    }

    //Линейный, двоичный поиск
    private boolean binarySearch(Item item, Comparator<Item> cmp) {
        int low = 0;
        int high = size - 1;
        while (low <= high) {
            int mid = low + (high - low) / 2; // (high + low) / 2
            if (cmp.compare(item, (Item) list[mid]) < 0) {
                high = mid - 1;
            }
            else if (cmp.compare(item, (Item) list[mid]) > 0) {
                low = mid + 1;
            }
            else { //cmp.compare(item, (Item) list[mid]) == 0
                return true;
            }
        }
        return false;
    }
}
