from icd11 import Icd11Fetcher


def main():
    fetcher = Icd11Fetcher()
    who_fic_foundation_vaccines_entity = "164949870"
    latest = fetcher.get_latest_release_for_entity(who_fic_foundation_vaccines_entity)
    descendants = fetcher.get_mms_descendants_for_entity(who_fic_foundation_vaccines_entity, latest)

    for mms_code, display in descendants.items():
        print(f'{mms_code}\t{display}')


if __name__ == "__main__":
    main()
