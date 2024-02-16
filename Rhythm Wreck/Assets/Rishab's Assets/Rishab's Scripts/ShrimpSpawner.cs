using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ShrimpSpawner : MonoBehaviour
{
    public static ShrimpSpawner Instance;
    [SerializeField] private GameObject FlyingShrimp;
    [SerializeField] private GameObject SwimmingShrimp;
    [SerializeField] private GameObject Canvas;
    public float CurrentTimeStamp {  get; private set; }

    void Start()
    {
        Instance = this;
    }

    public void SpawnFlyingShrimp(float timeStamp)
    {
        CurrentTimeStamp = timeStamp;
        Vector2 location = Camera.main.ViewportToWorldPoint(new Vector2(0.75f, 0.1f));
        GameObject flyingShrimp = (GameObject)Instantiate(FlyingShrimp);
        flyingShrimp.transform.SetParent(Canvas.transform);
        flyingShrimp.transform.position = location;
    }
    
    public void SpawnSwimmingShrimp(float timeStamp)
    {
        CurrentTimeStamp = timeStamp;
        Vector2 location = Camera.main.ViewportToWorldPoint(new Vector2(1f, 0.25f));
        GameObject swimmingShrimp = (GameObject)Instantiate(SwimmingShrimp);
        swimmingShrimp.transform.SetParent(Canvas.transform);
        swimmingShrimp.transform.position = location;
    }
}
