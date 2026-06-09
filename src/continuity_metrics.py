import pandas as pd

def continuity_scores(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute a simple continuity score (UPC-like) per patient.
    """
    provider_counts = df.groupby(['patient_id', 'doctor_id']).size().reset_index(name='encounters_with_provider')
    totals = provider_counts.groupby('patient_id')['encounters_with_provider'].sum().reset_index(name='total_encounters')
    max_counts = provider_counts.groupby('patient_id')['encounters_with_provider'].max().reset_index(name='max_provider_encounters')
    merged = totals.merge(max_counts, on='patient_id')
    merged['continuity_score'] = merged['max_provider_encounters'] / merged['total_encounters']
    return merged

def high_utilizers(df: pd.DataFrame, min_encounters: int = 4) -> pd.DataFrame:
    """
    Identify high-utilizer patients based on encounter count.
    """
    counts = df.groupby('patient_id').size().reset_index(name='encounter_count')
    return counts[counts['encounter_count'] >= min_encounters]
