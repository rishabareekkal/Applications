using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerController : MonoBehaviour
{
    public static PlayerController Instance;
    private Animator _animator;
    private SpriteRenderer[] _spriteRenderers;
    public bool LowerAttackable {  get; set; } = false;
    public bool UpperAttackable { get; set; } = false;
    public bool InTutorial { get; set; } = true;
    public bool Guiders { get; set; } = false;

    void Start()
    {
        Instance = this;
        _animator = gameObject.GetComponent<Animator>();
        _spriteRenderers = GetComponentsInChildren<SpriteRenderer>();
        LowerAttackable = false;
        UpperAttackable = false;
        InTutorial = true;
        Guiders = false;
    }

    void Update()
    {
        if (PauseManager.Instance.Paused)
        {
            foreach (SpriteRenderer spriteRenderer in _spriteRenderers)
            {
                if (!spriteRenderer.enabled) break;
                spriteRenderer.enabled = false;
            }
            return;
        }
        else
        {
            foreach (SpriteRenderer spriteRenderer in _spriteRenderers)
            {
                if (spriteRenderer.enabled) break;
                spriteRenderer.enabled = true;
            }
        }
        if (InTutorial)
        {
            LowerAttackable = true;
            UpperAttackable = true;
        }

        // From https://forum.unity.com/threads/start-animation-on-mouse-click.442023/ for animation setup.
        if (Input.GetKeyDown(KeyCode.UpArrow))
        {
            ResetAnim();
            _animator.StopPlayback();
            _animator.SetTrigger("High Swipe");
            if (!UpperAttackable)
            {
                ScoreHolder.Instance.Score -= 5;
            }
        }
        else if (Input.GetKeyDown(KeyCode.DownArrow))
        {
            ResetAnim();
            _animator.StopPlayback();
            _animator.SetTrigger("Low Swipe");
            if (!LowerAttackable)
            {
                ScoreHolder.Instance.Score -= 5;
            }
        }
    }

    public void ResetAnim()
    {
        if (_animator.GetCurrentAnimatorStateInfo(0).IsName("Low Swipe Anim") || _animator.GetCurrentAnimatorStateInfo(0).IsName("High Swipe Anim"))
        {
            _animator.SetTrigger("Idle");
        }
    }
}
