import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_population_evolution(population):
    """
    Affiche une courbe d'évolution pour les populations de poissons (fish) et de requins (sharks).
    
    Paramètres :
    population : list[tuple] - Liste de tuples (fish, sharks) à chaque étape de temps.
    """
    # Création du DataFrame
    df = pd.DataFrame(population, columns=['fish', 'sharks'])
    df['time'] = range(len(df))
    
    # Format long pour seaborn
    df_long = df.melt(id_vars='time', value_vars=['fish', 'sharks'], 
                      var_name='species', value_name='count')

    # Tracé
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 5))
    sns.lineplot(data=df_long, x='time', y='count', hue='species', marker='o')

    # Labels et titre
    plt.title("Évolution de la population de poissons et de requins")
    plt.xlabel("Temps")
    plt.ylabel("Nombre")
    plt.legend(title="Espèce")
    plt.tight_layout()
    plt.show()
