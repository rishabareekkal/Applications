using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Note : MonoBehaviour
{
    Rigidbody2D rb;
    public int speed;

    void Awake()
    {
        rb = GetComponent<Rigidbody2D>();
    }
     
    // Start is called before the first frame update
    void Start()
    {
        rb.velocity = new Vector2(0 , -speed);
    }

    // Update is called once per frame
    void Update()
    {
        if (EventManager.Paused)
        {
            
            rb.velocity = new Vector2(0, 0);
        }
        else
            rb.velocity = new Vector2(0, -speed);
    }
}
