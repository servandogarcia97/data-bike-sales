# === helpers ===
def inspect_categories(df, col, max_rows=50):
    temp = (
        df[col]
        .dropna()
        .to_frame("original")
        .assign(
            clean=lambda x: x["original"].str.strip().str.lower()
        )
        .drop_duplicates()
        .sort_values("clean")
    )

    n_original = temp.shape[0]
    n_clean = temp["clean"].nunique()
    
    conflicts = (
        temp
            .groupby("clean")["original"]
            .nunique()
            .reset_index(name="n_original")
            .query("n_original > 1")
    )
    if n_original == n_clean:
        print("No se detectan inconsistencias aparentes.")
    else:
        print("Hay inconsistencias entre original y clean (variantes sucias).")
        print(f"Grupos conflictivos: {conflicts.shape[0]}")

        if conflicts.shape[0] > 0:     
            problematic_clean = conflicts["clean"]
            problematic = temp[temp["clean"].isin(problematic_clean)]

            if len(problematic) > max_rows:
                print(f"\nMostrando primeros {max_rows} pares original/clean problemáticos:\n")
                display(problematic.head(max_rows))
            else:
                print("\nPares original/clean problemáticos:\n")
                display(problematic)

    return temp

def classify_age(age):
    age_cats = ['Adults (35-64)', 'Young Adults (25-34)', 'Youth (<25)']
    if age < 25:
        return age_cats[2]
    elif age < 35:
        return age_cats[1]
    else: 
        return age_cats[0]
    