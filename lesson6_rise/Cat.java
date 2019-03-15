package lesson6_rise;

import java.util.Random;

public class Cat extends Animal {

    //Конструктор
    public Cat(String name) {
        super(name);
    }

    //Метод сам определяет максимальное допустимое знаение для забега
    @Override
    public boolean run(double distance) {
        double x = random.nextInt(300) + 1;
        if (distance <= x) {
            System.out.println("Кот(-шка) " + getName() + " допущен(-а) к забегу на дистанцию до " + x + " метров(-а)");
            return true;
        }
        System.out.println("Кот(-шка) " + getName() + " не допущен(-а) к забегу на дистанцию более чем на " + x + " метров(-а)");
        return false;
    }

    //Коты не умеют плавать, поэтому всегда false
    @Override
    public boolean swim(double distance) {
        System.out.println("Коты не допускаются к заплыву.");
        return false;
    }

    //Метод сам определяет максимальное допустимое знаение для прыжка
    @Override
    public boolean jump(double distance) {
        double x = random.nextInt(4) + 1;
        if (distance <= x) {
            System.out.println("Кот(-шка) " + getName() + " допущен(-а) к прыжкам в высоту до " + x + " метров(-а)");
            return true;
        }
        System.out.println("Кот(-шка) " + getName() + " не допущен(-а) к прыжкам в высоту более чем на " + x + " метров(-а)");
        return false;
    }
}
