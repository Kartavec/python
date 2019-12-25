package Lesson1;


public abstract class Barrier {
    public abstract void doIt(Actions actions);
}

class Wall extends Barrier {

    int height;

    public Wall(int height) {
        this.height = height;
    }

    @Override
    public void doIt(Actions actions) {
        actions.jump(height);
    }
}

class RunningTrack extends Barrier {

    int length;

    public RunningTrack(int length) {
        this.length = length;
    }

    @Override
    public void doIt(Actions actions) {
        actions.run(length);
    }
}

