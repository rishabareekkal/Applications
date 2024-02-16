using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ImageCursor : NoteButtons
{
    public static ImageCursor Instance;

    public Image Hold;
    public Image Img1;
    public Image Img2;
    public Image Img3;
    public Image Img4;

    public Sprite None;
    public Sprite Grape;
    public Sprite Kiwi;
    public Sprite Pineapple;
    public Sprite Coconut;
    public Sprite Watermelon;
    public Sprite Banana;

    /*
These functions set the hold value to their respective fruits. They later get
added into the input list in the next funcitons
*/
    public override void SetValueToTa()
    {
        Hold.sprite = Grape;
    }
    public override void SetValueToTiti()
    {
        Hold.sprite = Kiwi;
    }
    public override void SetValueToTiTika()
    {
        Hold.sprite = Pineapple;
    }
    public override void SetValueToTikaTi()
    {
        Hold.sprite = Coconut;
    }
    public override void SetValueToTikaTika()
    {
        Hold.sprite = Watermelon;
    }
    public override void SetValueToTititi()
    {
        Hold.sprite = Banana;
    }
    /*
    These functions set values to their respective indexes of the input list based
    on the user input given in the previous funcitons.
    */

    public override void SetIndexValueOne()
    {
        if (NoteButtons.GetValue() - 1 == 0)
            Img1.sprite = Grape;
        else if (NoteButtons.GetValue() - 1 == 1)
            Img1.sprite = Kiwi;
        else if (NoteButtons.GetValue() - 1 == 2)
            Img1.sprite = Pineapple;
        else if (NoteButtons.GetValue() - 1 == 3)
            Img1.sprite = Coconut;
        else if (NoteButtons.GetValue() - 1 == 4)
            Img1.sprite = Watermelon;
        else
            Img1.sprite = Banana;

    }
    public override void SetIndexValueTwo()
    {
        if (NoteButtons.GetValue() - 1 == 0)
            Img2.sprite = Grape;
        else if (NoteButtons.GetValue() - 1 == 1)
            Img2.sprite = Kiwi;
        else if (NoteButtons.GetValue() - 1 == 2)
            Img2.sprite = Pineapple;
        else if (NoteButtons.GetValue() - 1 == 3)
            Img2.sprite = Coconut;
        else if (NoteButtons.GetValue() - 1 == 4)
            Img2.sprite = Watermelon;
        else
            Img2.sprite = Banana;
    }
    public override void SetIndexValueThree()
    {
        if (NoteButtons.GetValue() - 1 == 0)
            Img3.sprite = Grape;
        else if (NoteButtons.GetValue() - 1 == 1)
            Img3.sprite = Kiwi;
        else if (NoteButtons.GetValue() - 1 == 2)
            Img3.sprite = Pineapple;
        else if (NoteButtons.GetValue() - 1 == 3)
            Img3.sprite = Coconut;
        else if (NoteButtons.GetValue() - 1 == 4)
            Img3.sprite = Watermelon;
        else
            Img3.sprite = Banana;
    }
    public override void SetIndexValueFour()
    {
        if (NoteButtons.GetValue() - 1 == 0)
            Img4.sprite = Grape;
        else if (NoteButtons.GetValue() - 1 == 1)
            Img4.sprite = Kiwi;
        else if (NoteButtons.GetValue() - 1 == 2)
            Img4.sprite = Pineapple;
        else if (NoteButtons.GetValue() - 1 == 3)
            Img4.sprite = Coconut;
        else if (NoteButtons.GetValue() - 1 == 4)
            Img4.sprite = Watermelon;
        else
            Img4.sprite = Banana;
    }
    public void Reset()
    {
        Img1.sprite = None;
        Img2.sprite = None;
        Img3.sprite = None;
        Img4.sprite = None;
    }
    // Start is called before the first frame update
    void Start()
    {
        if (Instance == null)
            Instance = this;
    }

// Update is called once per frame
    void Update()
    {

    }
}
