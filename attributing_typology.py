import pandas as pd

def complete_user(user):

    # Load typologies
    df = pd.read_csv("BuildingTypo.csv", header=None)
    df.columns = ['Typo','Sh','Yc','Nf','Sj','Db','Eb','Ad','Hf','Hb','Hg','Sb','Sp','Tw','Ee','Er','Hcs', 'Yr']
    classifying = ['Sh','Yc','Nf','Sj','Db','Eb']
    optional = ['Ad','Hf','Hb','Hg','Sb','Sp','Tw','Ee','Er','Hcs', 'Yr']
    weight = [10, 8, 5, 4, 3, 1]

    for col in classifying:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Define the scoring function
    def score_typology(row, user, weight):
        score = 0
        for i, col in enumerate(classifying):
            if col in user and user[col] is not None:
                diff = abs(row[col] - user[col])
                score += weight[i] * diff
        return score

    # Compute scores and get best match
    df['Score'] = df.apply(lambda row: score_typology(row, user, weight), axis=1)
    best_typo = df.sort_values(by='Score').iloc[0]

    user_filled = user.copy()

    # Fill missing optional values
    for col in optional:
        if user_filled.get(col) is None:
            try:
                user_filled[col] = float(best_typo.get(col))
            except (ValueError, TypeError):
                user_filled[col] = best_typo.get(col)

    user_filled['Typology'] = best_typo['Typo']

    if 'Yr' not in user_filled or pd.isna(user_filled['Yr']):
        try:
            user_filled['Yr'] = float(user['Yc'])
        except (ValueError, TypeError):
            user_filled['Yr'] = user['Yc']

    return user_filled
