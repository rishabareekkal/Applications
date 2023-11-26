using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Events;

public class Attack2 : MonoBehaviour
{
    public static Attack2 Instance;
    private float cooldown;
    public float timeBtwAttack2 = 0.5f;

    public Transform attackPos2;
    public LayerMask whatIsEnemies2;
    public float attackRange2 = 1;
    public static int health2 = 1;
    public int knockback2 = health2;
    public int damage2 = 1;

    public Animator animator;

    public UnityEvent<GameObject> OnHit;

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

            if (Input.GetKey(KeyCode.Period))

            {

                Collider2D[] enemiesTodamage2 = Physics2D.OverlapCircleAll(attackPos2.position, attackRange2, whatIsEnemies2);
                enemiesTodamage2[0].GetComponent<Attack1>().Takedamage1(damage2, transform.gameObject);

                animator.SetBool("IsPunching", true);

                cooldown = timeBtwAttack2;
            }


        }
        else
        {
            cooldown -= Time.deltaTime;
            animator.SetBool("IsPunching", false);
        }
    }
    public void Takedamage2(int damage1, GameObject sender)
    {
        health2 += damage1;
        knockback2 = health2;
        KnockbackFeedback.strength = health2;
        if (health2 > 0)
        {
            OnHit?.Invoke(sender);
        }
    }
}