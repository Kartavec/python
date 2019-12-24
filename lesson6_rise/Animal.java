package lesson6_rise;

import java.text.DecimalFormat;
import java.util.Random;

abstract class Animal {

    //Параметр - дистанция
    private double distance;
    private String name;

    Random random = new Random();

    //Действия - бег,плаванье,прыжок
    public abstract boolean run(double distance);
    public abstract boolean swim(double distance);
    public abstract boolean jump(double distance);

    //Вывести имя
    public String getName() {
        return name;
    }

    //Задать имя
    public void setName(String _name) {
        this.name = _name;
    }

    //Конструктор
    public Animal(String name) {
        this.name = name;
    }
}
