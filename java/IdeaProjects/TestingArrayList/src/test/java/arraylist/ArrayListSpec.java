package arraylist;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;

public class ArrayListSpec {
    private List<String> stringList;

    @BeforeEach
    void init(){
        stringList = new ArrayList<String>();
    }

    @Test
    public void emptyList(){
        assertTrue(stringList.isEmpty(), "List now must be empty.");
    }

    @Test
    public void emptyListAfterAddAndRemove(){
        stringList.add("Assembly");
        stringList.remove("Assembly");
        assertTrue(stringList.isEmpty(), "List must be empty by now.");
    }
    @Test
    public void getReturnActualValue(){
        stringList.add("C++")
;        assertEquals(0, stringList.indexOf("C++"));
    }
    @Test
    public void containsElements(){
        stringList.add("Assembly");
        assertEquals("Assembly", stringList.get(0), "The value must be <Assembly>");
    }



}
