using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class HealthBar : MonoBehaviour
{
    public static HealthBar Instance;
    [SerializeField] private Image _healthBar;
    [SerializeField] private float _healthAmount = 100f;
    private const float _damage = 10f;

    void Start()
    {
        Instance = this;
    }

    public void TakeDamage()
    {
        _healthAmount -= _damage;
        _healthBar.fillAmount = _healthAmount / 100f;
        if (_healthAmount <= 0 ) {
            GameOverScreen.Instance.GameOver();
        }
    }
}
