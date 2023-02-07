package designpattern;

import java.io.*;

public class Singleton {
    /*
    시스템 런타임, 환경 세팅에 대한 정보 등, 인스턴스가 여러개 일 때 문제가 생길 수 있는 경우기 있다.
    인스턴스를 오직 한개만 만들어 제공하는 클래스가 필요하다.
     */

    public static void main(String[] args) {
        TObject tObject = TObject.INSTANCE;
        TObject tObject1 = TObject.INSTANCE;

        System.out.println(tObject1 == tObject);

    }







//    public static void main(String[] args) {
//        System.out.println(TObject.class);
//        TObject object = TObject.getInstance();
//        TObject object1 = TObject.getInstance();
//
//
//        System.out.println(object == object1);
//
//    }


//    public static void main(String[] args) throws NoSuchMethodException, InvocationTargetException, InstantiationException, IllegalAccessException {
//        TObject tObject = TObject.getInstance();
//        Constructor<TObject> contructor = TObject.class.getDeclaredConstructor();
//        contructor.setAccessible(true);
//        TObject tObject1 = contructor.newInstance();
//        System.out.println(tObject1 == tObject);
//
//    }


//    public static void main(String[] args) {
//        TObject tObject = TObject.getInstance();
//        TObject tObject1 = null;
//        try (ObjectOutput out = new ObjectOutputStream(new FileOutputStream("TObject.obj"))) {
//            out.writeObject(tObject);
//        } catch (FileNotFoundException e) {
//            throw new RuntimeException(e);
//        } catch (IOException e) {
//            throw new RuntimeException(e);
//        }
//
//        try (ObjectInput in = new ObjectInputStream(new FileInputStream("TObject.obj"))) {
//            tObject1 = (TObject) in.readObject();
//        } catch (FileNotFoundException e) {
//            throw new RuntimeException(e);
//        } catch (IOException e) {
//            throw new RuntimeException(e);
//        } catch (ClassNotFoundException e) {
//            throw new RuntimeException(e);
//        }
//        System.out.println(tObject1 == tObject);
//
//    }
}

enum TObject {
    INSTANCE;

    TObject() {

    }


}

/*class TObject implements Serializable {
    private TObject() {

    }

    private static class SettingsHolder {
        private static final TObject INSTANCE = new TObject();
    }

    public static TObject getInstance() {
        return SettingsHolder.INSTANCE;
    }

    protected TObject readResolve() {
        return getInstance();
    }


}*/


//class TObject {
//    private static volatile TObject instance;
//    /*
//    volatile : 변수를 메인 메모리에 저장하겠다!
//
//
//     */
//    private static TObject getInstance() {
//        if (instance == null) {
//            synchronized (TObject.class) {
//                if (instance == null) {
//                    instance = new TObject();
//                }
//            }
//        }
//        return instance;
//    }
//    private TObject() {
//
//    }
//
//    public static TObject getTObject() {
//        return new TObject();
//    }
//
//}

//class TObject {
//    private final static TObject INSTANCE = new TObject();
//    private static TObject getInstance() {
//        return INSTANCE;
//    }
//    private TObject() {
//
//    }
//
//    public static TObject getTObject() {
//        return new TObject();
//    }
//
//}



//class TObject {
//    private static TObject instance;
//    private static synchronized TObject getInstance() {
//        if (instance == null) {
//            instance = new TObject();
//        }
//        return instance;
//    }
//    private TObject() {
//
//    }
//
//    public static TObject getTObject() {
//        return new TObject();
//    }
//
//}