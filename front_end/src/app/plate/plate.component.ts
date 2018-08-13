import { Component, OnInit } from '@angular/core';
import { ChromPackService } from '../services/chrompack.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-plate',
  templateUrl: './plate.component.html',
  styleUrls: ['./plate.component.css']
})
export class PlateComponent implements OnInit {

  refreshMetricsSubscription: Subscription
  slotsSettings: any;
  chrompacks: any;
  idSelected: String;

  constructor(private chrompackService: ChromPackService) { }

  ngOnInit() {

    if(!this.idSelected){
      this.fillSettingsDefault();
    }
  }

  fillSettingsDefault() {
    this.slotsSettings = [
      [false, false, false, false, false, false, false, false],
      [false, false, false, false, false, false, false, false],
      [false, false, false, false, false, false, false, false],
      [false, false, false, false, false, false, false, false],
      [false, false, false, false, false, false, false, false],
      [false, false, false, false, false, false, false, false],
      [false, false, false, false, false, false, false, false],
      [false, false, false, false, false, false, false, false]
    ];
  }

  viewSlots(id){
    

    this.idSelected = id;

    this.chrompackService.getSlots(this.idSelected).subscribe(result => {
      this.slotsSettings = result;
    }, err => {
      //TODO exibir modal de erro
    });
  }

}
