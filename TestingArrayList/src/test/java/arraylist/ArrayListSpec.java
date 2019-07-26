package arraylist;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class ArrayListSpec {
    private List<Languages> JVMLang;

    @BeforeEach
    void init(){
        JVMLang = new ArrayList<>();
    }


    @Test
    @DisplayName("ADDMethod - index and values.")
    public void containsADDedEntry(){
        JVMLang.add(Languages.CPP);
        assertEquals(1,JVMLang.size(), "Size must be 1.");
        assertEquals(Languages.CPP, JVMLang.get(0), " Should print the current Value - CPP.");

        JVMLang.add(Languages.KAWA);//Add one more element to make 2
        assertEquals(2,JVMLang.size(), "Size must increase to 2.");
        assertEquals(Languages.CPP, JVMLang.get(0), "First added element must still be there.");
        assertEquals(Languages.KAWA, JVMLang.get(1), "So is the subsequent added elements.");

        JVMLang.add(Languages.CPP);
        JVMLang.add(Languages.SCALA);
        JVMLang.add(Languages.KAWA);
        JVMLang.add(Languages.KOTLIN);
        JVMLang.add(Languages.PROCESSING);

        assertEquals(7, JVMLang.size(), "Element Added at the correct index.");

        JVMLang.add(5, Languages.FANTOM);
        assertEquals(Languages.FANTOM, JVMLang.get(5));
        assertEquals(8, JVMLang.size(), "Size appropriately increase.");

    }

    @Test
    public void EMPTYList(){
        assertTrue(JVMLang.isEmpty(), "List now must be empty.");
        assertTrue(JVMLang.add(Languages.SCALA));
        assertTrue(JVMLang.remove(Languages.SCALA));
        assertTrue(JVMLang.isEmpty(), "List must be empty by now.");
    }

    @Test
    public void CONTAINSElements(){
        JVMLang.add(Languages.CPP);
        assertTrue(JVMLang.contains(Languages.CPP));
        assertEquals(Languages.CPP, JVMLang.get(0), "The value must be CPP.");
    }

    @Test
    @DisplayName("ADDALLCollections - Indexes and Values")
    public void ADDALLCollections(){
        assertTrue(JVMLang.addAll(Arrays.asList(Languages.values())), "True if collection was added Successfully.");
        assertEquals(11, JVMLang.size());
        assertEquals(Languages.values().length, JVMLang.size(), "Length of Enum and Array size must be equal.");
        assertTrue(JVMLang.contains(Languages.SCALA), "Contains a particular element after addAll");
        assertTrue(JVMLang.containsAll(Arrays.asList(Languages.values())), "Contains collection all added elements");

        assertTrue(JVMLang.addAll(10, Arrays.asList(Languages.values())), "Collection successfully added at index");
        assertEquals(Languages.values().length*2, JVMLang.size(), "Size should double after adding Collection twice");
        assertEquals(22, JVMLang.size());
        assertEquals(JVMLang.lastIndexOf(Languages.KAWA), 21);
    }



}
