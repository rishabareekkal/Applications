using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class moveWASD : MonoBehaviour
{
    public float move_speed = 5;
    public float rotationSpeed = 400;

    float movementX;
    float movementY;


    Rigidbody2D rb;



    // Start is called before the first frame update
    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
        movementX = 0;
        movementY = 0;
    }

    // Update is called once per frame
    void Update()
    {
        if (Countdown.gameStart == true)
        { 
            Vector3 moveDir = new Vector3(movementX, movementY).normalized;

            transform.position += moveDir * move_speed * Time.deltaTime;

            if (Input.GetKeyDown(KeyCode.W))
            {
                movementY += 1;
            }
            if (Input.GetKeyUp(KeyCode.W))
            {
                movementY -= 1;
            }
            if (Input.GetKeyDown(KeyCode.S))
            {
                movementY -= 1;
            }
            if (Input.GetKeyUp(KeyCode.S))
            {
                movementY += 1;
            }
            if (Input.GetKeyDown(KeyCode.D))
            {
                movementX += 1;
            }
            if (Input.GetKeyUp(KeyCode.D))
            {
                movementX -= 1;
            }
            if (Input.GetKeyDown(KeyCode.A))
            {
                movementX -= 1;
            }
            if (Input.GetKeyUp(KeyCode.A))
            {
                movementX += 1;
            }
                if (moveDir != Vector3.zero)
                {

                    Quaternion toRotation = Quaternion.LookRotation(Vector3.forward, moveDir);
                    transform.rotation = Quaternion.RotateTowards(transform.rotation, toRotation, rotationSpeed * Time.deltaTime);
                }
        }

    }

}
