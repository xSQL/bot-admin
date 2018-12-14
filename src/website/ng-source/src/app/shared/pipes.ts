import { Pipe, PipeTransform } from '@angular/core';

@Pipe({name: 'substring'})
export class SubstringPipe implements PipeTransform {
  transform(value: string, limit: number): any {
    if(value.length<=limit) {
      return value
    } else {
      return value.substring(0, limit) + '...';
    }
  }
}
