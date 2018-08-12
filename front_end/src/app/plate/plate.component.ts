import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { UploadComponent } from '../upload/upload.component';
import { ChromPackService } from '../services/chrompack.service';
import { ChrompackServiceObservable } from '../services/chrompack-observable.service';
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

  constructor(private modalService: NgbModal,
              private chrompackService: ChromPackService,
              private chrompackServiceObservable: ChrompackServiceObservable) { }

  ngOnInit() {

    this.refreshMetricsSubscription = this.chrompackServiceObservable.getRefreshResult().subscribe(() => {
      this.getChrompackList();
    });

    if(!this.idSelected){
      this.fillSettingsDefault();
    }

    this.getChrompackList();
  }

  getChrompackList() {
    this.chrompackService.getList().subscribe(result => {
      this.chrompacks = result;
    }, err => {
      //TODO exibir modal de erro
    });
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
    this.chrompacks.forEach(chrompack => {

      if(chrompack._id === this.idSelected) {
        chrompack.selected = false;
      }
      
      if(chrompack._id === id) {
        chrompack.selected = true;
      }
    });

    this.idSelected = id;

    this.chrompackService.getSlots(this.idSelected).subscribe(result => {
      this.slotsSettings = result;
    }, err => {
      //TODO exibir modal de erro
    });
  }

  addChrompack(){
    this.modalService.open(UploadComponent);
  }

  deleteChrompack() {
    this.chrompackService.delete(this.idSelected).subscribe(() => {
      this.getChrompackList();
      this.chrompackServiceObservable.sendRefreshResult();
    }, err => {
      //TODO exibir modal de erro
    });
  }

}
