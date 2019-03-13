import java.util.Random;
import java.util.Scanner;

public class lesson_4 {

    //параметы игрового поля
    static int size_x = 6; //размер поля по вертикали
    static int size_y = 6; //размер поля по горизонтали
    static int size_win; //количество заполненных полей для победы. Задается пользователем
    static char[][] field = new char[size_y][size_x];

    // игровые элементы
    static char playerDot = 'X';
    static char aiDot = 'O';
    static char emptyDot = ' ';

    //объявление классов ввода и случайного числа для игры
    static Scanner sc = new Scanner(System.in);
    static Random rand = new Random();

    public static void main(String[] args) {

        initField();
        printField();
        setSizeWin();

        do {
            playerStep();
            printField();
            if (checkWin(playerDot)){
                System.out.println("Вы выиграли!");
                break;
            }
            else if (isFieldFull()){
                break;
            }

            aiStep();
            printField();
            if (checkWin(aiDot)){
                System.out.println("Вы проиграли!");
                break;
            }
            else if (isFieldFull()){
                break;
            }
        } while (true);
        System.out.println("!Конец игры!");
    }

    //получение размера выигрышной комбинации
    public static void setSizeWin(){
        System.out.print("Введие количество символов подряд для победы: ");
        size_win = sc.nextInt();
        if (size_win > size_x || size_win > size_y){
            do {
                System.out.print("Введено недопустимое значение. Повторите ввод: ");
                size_win = sc.nextInt();
            } while (size_win > size_x && size_win > size_y);
        }
    }

    //метод для заполнения поля пустыми значениями в начале игры
    public static void initField(){
        for (int i = 0; i < size_y; i++){
            for (int j = 0; j < size_x; j++){
                field[i][j] = emptyDot;
            }
        }
    }

    //метод для вывода поля на консоль
    public static void printField(){

        int count = 0;
        StringBuilder sb_x = new StringBuilder("  -");
        do {
            count += 1;
            sb_x.append(count);
            sb_x.append("-");
        } while (count != size_x);

        System.out.println(sb_x);
        count = 1;

        for (int i = 0; i < size_y; i++) {
            System.out.print(count + " ");
            count += 1;
            System.out.print("|");
            for (int j = 0; j < size_x; j++) {
                System.out.print(field[i][j] + "|");
            }
            System.out.println();
        }
    }

    //метод для установки символа
    public static void setSym(int y, int x, char Sym){
        field[y][x] = Sym;
    }

    //метод для проверки попадания координат в заданное поле
    public static boolean isCellValid(int y, int x){
        if (x < 0 || y < 0 || x > size_x - 1 || y > size_y - 1){
            return false;
        }
        return field[y][x] == emptyDot;
    }

    //Ход игрока
    public static void playerStep(){
        int x, y;
        do {
            System.out.print("Введите номер столбца (от 1 до " + size_x + "):");
            x = sc.nextInt() - 1;
            System.out.print("Введите номер строки (от 1 до " + size_y + "):");
            y = sc.nextInt() - 1;
            if (!isCellValid(y,x)){
                System.out.println("Введены некорректные параметры. Повторите ввод.");
            }
        } while (!isCellValid(y,x));
        setSym(y, x, playerDot);
    }

    //Ход компьютера
    public static void aiStep(){
        int x, y;
        int trueDot;
        //блокировка выигрышного хода человека по горизонтали и вертикали
        for (int i = 0; i < size_y; i++) {
            for (int j = 0; j < size_x; j++) {
                //анализ наличия поля для проверки
                if (i + size_win <= size_y) {                           //по вертикали
                    if (checkLineVertical(i, j, playerDot) >= 2) {
                        if(MoveAiLineVertical(i + 1, j, aiDot)) return;
                    }
                }
                if (j + size_win <= size_x) {                           //по горизонтали
                    if (checkLineHorisont(i, j, playerDot) >= 2) {
                        if (MoveAiLineHorisont(i, j + 1, aiDot)) return;
                    }
                }
            }
        }
        //блокировка выигрышного хода человека по диагонали
        for (int i = 0; i < size_y; i++) {
            for (int j = 0; j < size_x; j++) {
                //анализ наличия поля для проверки
                if (j + size_win <= size_x) {
                    if (i - size_win > -2) {                            //вверх по диагонали
                        if (checkDiaUp(i, j, playerDot) >= 2) {
                            if (MoveAiDiaUp(i + 1, j + 1, aiDot)) return;
                        }
                    }
                    if (i + size_win <= size_y) {                       //вниз по диагонали
                        if (checkDiaDown(i, j, playerDot) >= 2) {
                            if (MoveAiDiaDown(i + 1, j + 1, aiDot)) return;
                        }
                    }
                }
            }
        }
        //игра на победу по горизонтали и вертикали
        for (int i = 0; i < size_y; i++) {
            for (int j = 0; j < size_x; j++) {
                //анализ наличия поля для проверки
                if (i + size_win <= size_y) {                           //по вертикали
                    if (checkLineVertical(i, j, aiDot) >= 2) {
                        if(MoveAiLineVertical(i + 1, j, aiDot)) return;
                    }
                }
                if (j + size_win <= size_x) {                           //по горизонтали
                    if (checkLineHorisont(i, j, aiDot) >= 2) {
                        if (MoveAiLineHorisont(i, j + 1, aiDot)) return;
                    }
                }
            }
        }
        //игра на победу по диагонали
        for (int i = 0; i < size_y; i++) {
            for (int j = 0; j < size_x; j++) {
                //анализ наличия поля для проверки
                if (j + size_win <= size_x) {
                    if (i - size_win > -2) {                            //вверх по диагонали
                        if (checkDiaUp(i, j, aiDot) >= 2) {
                            if (MoveAiDiaUp(i + 1, j + 1, aiDot)) return;
                        }
                    }
                    if (i + size_win <= size_y) {                       //вниз по диагонали
                        if (checkDiaDown(i, j, aiDot) >= 2) {
                            if (MoveAiDiaDown(i + 1, j + 1, aiDot)) return;
                        }
                    }
                }
            }
        }
        //случайный ход
        do {
            x = rand.nextInt(size_x);
            y = rand.nextInt(size_y);
        } while (!isCellValid(y,x));
        setSym(y, x, aiDot);
    }

    //ход компьютера по горизонтали
    private static boolean MoveAiLineHorisont(int v, int h, char dot) {
        for (int j = h; j < size_win; j++) {
            if ((field[v][j] == emptyDot)) {
                field[v][j] = dot;
                return true;
            }
        }
        return false;
    }

    //ход компьютера по вертикали
    private static boolean MoveAiLineVertical(int v, int h, char dot) {
        for (int i = v; i<size_win; i++) {
            if ((field[i][h] == emptyDot)) {
                field[i][h] = dot;
                return true;
            }
        }
        return false;
    }

    //проверка заполнения всей линии по диагонали вверх
    private static boolean MoveAiDiaUp(int v, int h, char dot) {
        for (int i = 0, j = 0; j < size_win; i--, j++) {
            if ((field[v+i][h+j] == emptyDot)) {
                field[v+i][h+j] = dot;
                return true;
            }
        }
        return false;
    }

    //проверка заполнения всей линии по диагонале вниз
    private static boolean MoveAiDiaDown(int v, int h, char dot) {
        for (int i = 0; i < size_win - 1; i++) {
            if ((field[i + v][i + h] == emptyDot)) {
                field[i + v][i + h] = dot;
                return true;
            }
        }
        return false;
    }

    //определение ничьей
    public static boolean isFieldFull(){
        for (int i = 0; i < size_y; i++){
            for (int j = 0; j < size_x; j++){
                if (field[i][j] == emptyDot){
                    return false;
                }
            }
        }
        System.out.println("Игра закончилась в ничью");
        return true;
    }

    //проверка на победу
    private static boolean checkWin(char sym) {
        for (int i = 0; i < size_y; i++){
            for (int j = 0; j < size_x; j++) {
                //анализ наличие поля для проверки
                if (j + size_win <= size_x) {                           //по горизонтале
                    if (checkLineHorisont(i, j, sym) >= size_win) {
                        return true;
                    }

                    if (i - size_win > -2) {                            //вверх по диагонале
                        if (checkDiaUp(i, j, sym) >= size_win) {
                            return true;
                        }
                    }
                    if (i + size_win <= size_y) {                       //вниз по диагонале
                        if (checkDiaDown(i, j, sym) >= size_win) {
                            return true;
                        }
                    }
                }
                if (i + size_win <= size_y) {                       //по вертикали
                    if (checkLineVertical(i, j, sym) >= size_win) {
                        return true;
                    }
                }
            }
        }
        return false;
    }

    //проверка заполнения всей линии по диагонале вверх
    private static int checkDiaUp(int v, int h, char dot) {
        int count=0;
        for (int i = 0, j = 0; j < size_win; i--, j++) {
            if ((field[v+i][h+j] == dot)) count++;
            else if ((field[v+i][h+j] != emptyDot)) {
                break;
            }
            else count = 0;
        }
        return count;
    }

    //проверка заполнения всей линии по диагонале вниз
    private static int checkDiaDown(int v, int h, char dot) {
        int count=0;
        for (int i = 0; i < size_win; i++) {
            if ((field[i+v][i+h] == dot)) count++;
        }
        return count;
    }

    private static int checkLineHorisont(int v, int h, char dot) {
        int count=0;
        for (int j = h; j < size_win + h; j++) {
            if ((field[v][j] == dot)) count++;
        }
        return count;
    }

    //проверка заполнения всей линии по вертикале
    private static int checkLineVertical(int v, int h, char dot) {
        int count=0;
        for (int i = v; i< size_win + v; i++) {
            if ((field[i][h] == dot)) count++;
        }
        return count;
    }
}
