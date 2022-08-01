import { Component, Input, OnInit } from '@angular/core';
import { DataService } from 'src/app/shared/data.service';

@Component({
  selector: 'app-slider',
  templateUrl: './slider.component.html',
  styleUrls: ['./slider.component.scss']
})
export class SliderComponent implements OnInit {
  @Input() uuid!: string
  value!: number;

  constructor(private dataService: DataService) { }

  ngOnInit(): void {
  }

  isInverted(){
    return this.dataService.slider_data.get(this.uuid)?.invert as boolean
  }

  isMax(){
    return this.dataService.slider_data.get(this.uuid)?.max as number
  }

  isMin(){
    return this.dataService.slider_data.get(this.uuid)?.min as number
  }

  step(){
    return this.dataService.slider_data.get(this.uuid)?.step as number
  }

  isThumbLabel(){
    return this.dataService.slider_data.get(this.uuid)?.thumbLabel as boolean
  }

  isVertical(){
    return this.dataService.slider_data.get(this.uuid)?.vertical as boolean
  }

}