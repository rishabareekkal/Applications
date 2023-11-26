using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Events;

public class Attack1 : MonoBehaviour
{
    public static Attack1 Instance;
    private float cooldown;
    public float timeBtwAttack1 = 0.5f;

    public Transform attackPos1;
    public LayerMask whatIsEnemies1;
    public float attackRange1 = 1;
    public static int health1 = 1;
    public int knockback1 = health1;
    public int damage1 = 1;

    public Animator animator;


    public UnityEvent<GameObject> OnHit;

    // Update is called once per frame
    void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
            DontDestroyOnLoad(gameObject);
        }
        else
        {
            Destroy(gameObject);
        }
    }

    void Update()
    {

        if (cooldown <= 0)
        {

            if (Input.GetKey(KeyCode.E))

            {
                Collider2D[] enemiesTodamage1 = Physics2D.OverlapCircleAll(attackPos1.position, attackRange1, whatIsEnemies1);
                enemiesTodamage1[0].GetComponent<Attack2>().Takedamage2(damage1, transform.gameObject);

                animator.SetBool("IsPunching", true);

                cooldown = timeBtwAttack1;


            }

        }
        else
        {
            cooldown -= Time.deltaTime;
            animator.SetBool("IsPunching", false);
        }
    }
    public void Takedamage1(int damage2, GameObject sender)
    {
        health1 += damage2;
        knockback1 = health1;
        KnockbackFeedback.strength = health1;
        if (health1 > 0)
        {
            OnHit?.Invoke(sender);
        }
    }
}