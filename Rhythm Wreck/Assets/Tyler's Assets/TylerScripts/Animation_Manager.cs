using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Animation_Manager : MonoBehaviour
{
    public Animator animator;
    // Start is called before the first frame update
    void Start()
    {
        animator = GetComponent<Animator>();
    }

    // Update is called once per frame
    void Update()
    {
        if (NoteActuator.Combo == 0)
        {
            animator.SetBool("if_missed", true);
        }
        else if (NoteActuator.Combo >= 5)
            animator.SetBool("if_missed",false);
    }
}
