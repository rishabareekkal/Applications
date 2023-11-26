using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Events;

public class KnockbackFeedback : MonoBehaviour
{

    [SerializeField]
    private Rigidbody2D rb;


    public static float strength = 1, delay = .15f;

    public UnityEvent OnBegin, Ondone;

    public void PlayFeedback(GameObject sender)
    {
        StopAllCoroutines();
        OnBegin?.Invoke();
        Vector3 direction = (transform.position - sender.transform.position).normalized;
        rb.AddForce(direction * strength, ForceMode2D.Impulse);
        StartCoroutine(Reset());


    }

    private IEnumerator Reset()
    {
        yield return new WaitForSeconds(delay);
        rb.velocity = Vector3.zero;
        Ondone?.Invoke();
    }
}