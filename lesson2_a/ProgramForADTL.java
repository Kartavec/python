package lesson2;

import java.util.Random;

public class ProgramForADTL {

    private static final int amountOfElements = 1000; //Количество элементов в списке
    private static final int numberOfRepetitions = 20; //Количество повторений сортировок

    private static final long[] timeSelectionSort = new long[numberOfRepetitions]; //Массив для хранения времени работы сортировки выбором
    private static final long[] timeInsertionSort = new long[numberOfRepetitions]; //Массив для хранения времени работы сортировки вставками

    public static Random random = new Random();

    private static long timeConsumedMillis1;
    private static long timeConsumedMillis2;

    public static void main(String[] args) {

        AbstractDataTypeList<Character> list = new AbstractDataTypeList<>();

        //Заполнение списка буквами в диапозоне от a до z
        for (int j = 0; j < amountOfElements; j++) {
            char n = (char) (random.nextInt(26) + 'a');
            list.add(n);
        }

        System.out.println("Сортировка" + "\t" + "Сортировка");
        System.out.println(" выбором" + "    " + "вставками");
        for (int i = 0; i < numberOfRepetitions; i++) {
            timeSelection(list);
            timeSelectionSort[i] = timeConsumedMillis1;

            for (int j = 0; j < amountOfElements; j++) {
                char n = (char) (random.nextInt(26) + 'a');
                list.set(j, n);
            }
        }

        for (int i = 0; i < numberOfRepetitions; i++) {
            timeInsertion(list);
            timeInsertionSort[i] = timeConsumedMillis2;

            for (int j = 0; j < amountOfElements; j++) {
                char n = (char) (random.nextInt(26) + 'a');
                list.set(j, n);
            }
        }

        for (int i = 0; i < numberOfRepetitions; i++) {
            System.out.println("\t" + timeSelectionSort[i] + "\t" + "\t" + "\t" + timeInsertionSort[i]);
        }
    }

    //Сортировка выбором
    public static long timeSelection(AbstractDataTypeList<Character> list){
        long start = System.currentTimeMillis();
        list.selectionSort(Character::compareTo);
        long finish = System.currentTimeMillis();
        timeConsumedMillis1 = finish - start;
        return timeConsumedMillis1;

        }

    //Сортировка вставками
    public static long timeInsertion(AbstractDataTypeList<Character> list){
        long start = System.currentTimeMillis();
        list.insertionSort(Character::compareTo);
        long finish = System.currentTimeMillis();
        timeConsumedMillis2 = finish - start;
        return timeConsumedMillis2;
    }
    }

