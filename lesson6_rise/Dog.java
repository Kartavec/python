package lesson6_rise;

public class Dog extends Animal{

        //Конструктор
        public Dog(String name) {
            super(name);
        }

        @Override
        public boolean run(double distance) {
            double x = random.nextInt(500) - 1;
            if (distance <= x) {
                System.out.println("Собака " + getName() + " допущена к забегу до " + x + " метров(-а)");
                return true;
            }
            System.out.println("Собака " + getName() + " не допущена к забегу более чем на " + x + " метров(-а)");
            return false;
        }

        @Override
        public boolean swim(double distance) {
            double x = random.nextInt(500) + 1;
            if (distance <= x) {
                System.out.println("Собака " + getName() + " допущена к заплыву до " + x + " метров(-а)");
                return true;
            }
            System.out.println("Собака " + getName() + " не допущена к заплыву более чем на " + x + " метров(-а)");
            return false;
        }

        @Override
        public boolean jump(double distance) {
            double x = random.nextInt(2) + 1;
            if (distance <= x) {
                System.out.println("Собака " + getName() + " допущена к прыжкам в высоту до " + x + " метров(-а)");
                return true;
            }
            System.out.println("Собака " + getName() + " не допущена к прыжкам в высоту более чем на " + x + " метров(-а)");
            return false;
        }
    }
