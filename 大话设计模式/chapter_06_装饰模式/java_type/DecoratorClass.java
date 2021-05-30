package Test;

/**
 * @author william_x_f_wang
 * @email 1016795105@qq.com
 * @Date 2021/5/28、1:42
 * description
 * @since
 */


public class DecoratorClass extends TargetClass{

    private TargetClass myTarget;

    public void setTarget(TargetClass target) {
        myTarget = target;
    }

    public void operation() {
        System.out.println("i am DecoratorClass class");
        myTarget.operation();
    }
}
