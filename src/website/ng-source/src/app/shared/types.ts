export class CrudAction {
  public label: string;
  public title: string;
}

export class GroupItem {
  public pk: number;
  public name: string;
  public community_id: string;
}

export class SynonymItem {
  public pk: number;
  public name: string;
  public value: string;
  public community_id: string;
}

export class SynonymPagination {
  public count: number;
  public next: string;
  public previous: string;
  public results: SynonymItem[];
}

export class UserItem {
  public first_name: string;
  public middle_name: string;
  public last_name: string;
  public phone: string;
  public skype: string;
  public telegram: string;
}

