package arrayListT;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class ArrayListSpec {
    private List<String> stringList;

    @BeforeEach
    void init(){
        stringList = new ArrayList<>();
    }
    @Test
    public void empArrayList(){
        assertTrue(stringList.isEmpty(), "ArrayList must be empty.");
    }
    @Test
    public void oneElementInList(){
        stringList.add("Assembly");
        assertEquals(1, stringList.size());
    }
}
