using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class moveArrows : MonoBehaviour
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

            if (Input.GetKeyDown(KeyCode.UpArrow))
            {
                movementY += 1;
            }
            if (Input.GetKeyUp(KeyCode.UpArrow))
            {
                movementY -= 1;
            }
            if (Input.GetKeyDown(KeyCode.DownArrow))
            {
                movementY -= 1;
            }
            if (Input.GetKeyUp(KeyCode.DownArrow))
            {
                movementY += 1;
            }
            if (Input.GetKeyDown(KeyCode.RightArrow))
            {
                movementX += 1;
            }
            if (Input.GetKeyUp(KeyCode.RightArrow))
            {
                movementX -= 1;
            }
            if (Input.GetKeyDown(KeyCode.LeftArrow))
            {
                movementX -= 1;
            }
            if (Input.GetKeyUp(KeyCode.LeftArrow))
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
