using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class P2InBound : MonoBehaviour
{
    [SerializeField] private CircleCollider2D _ring;

    private void OnTriggerExit2D(Collider2D collision)
    {
        if (collision.gameObject.name == "Ring Area")
        {

            WinScreens.Instance.p1Win = true;
            WinScreens.Instance.GameFinished();


        }
    }
}
