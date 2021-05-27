package Test;

/**
 * @author william_x_f_wang
 * @email 1016795105@qq.com
 * @Date 2021/5/28、1:38
 * description
 * @since
 */
public class Test {
    public static void main(String[] args) {
        TargetClass target = new TargetClass();
        DecoratorClass d = new DecoratorClass();

        d.setTarget(target);
        d.operation();
    }
}
