import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { UploadComponent } from '../upload/upload.component';
import { ChromPackService } from '../services/chrompack.service';

@Component({
  selector: 'app-plate',
  templateUrl: './plate.component.html',
  styleUrls: ['./plate.component.css']
})
export class PlateComponent implements OnInit {

  slotsSettings: any;
  chrompacks: any;
  idSelected: String;

  constructor(private modalService: NgbModal,
              private chrompackService: ChromPackService) { }

  ngOnInit() {

    if(!this.idSelected){
      this.fillSettingsDefault();
    }

    this.chrompacks = [
      {
        filename: "teste_one_samples.zip",
        id: "5acbc564bdsa7c5"
      },
      {
        filename: "teste_one_samples.zip",
        id: "5acbc564bdsa7c6"
      },
      {
        filename: "teste_one_samples.zip",
        id: "5acbc564bdsa7c7"
      },
      {
        filename: "teste_one_samples.zip",
        id: "5acbc564bdsa7c8"
      },
      {
        filename: "teste_one_samples.zip",
        id: "5acbc564bdsa7c9"
      },
      {
        filename: "teste_one_samples.zip",
        id: "5acbc564bdsa710"
      },
      {
        filename: "teste_one_samples.zip",
        id: "5acbc564bdsa711"
      },
      {
        filename: "teste_one_samples.zip",
        id: "5acbc564bdsa712"
      },
      {
        filename: "teste_one_samples.zip",
        id: "5acbc564bdsa713"
      },
      {
        filename: "teste_one_samples.zip",
        id: "5acbc564bdsa714"
      },
      {
        filename: "teste_one_samples.zip",
        id: "5acbc564bdsa715"
      },
      {
        filename: "teste_one_samples.zip",
        id: "5acbc564bdsa716"
      },
      {
        filename: "teste_one_samples.zip",
        id: "5acbc564bdsa717"
      },
      {
        filename: "teste_one_samples.zip",
        id: "5acbc564bdsa718"
      },
      {
        filename: "teste_one_samples.zip",
        id: "5acbc564bdsa719"
      }
    ];
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

      if(chrompack.id === this.idSelected) {
        chrompack.selected = false;
      }
      
      if(chrompack.id === id) {
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
    this.chrompackService.delete(this.idSelected).subscribe(result => {
      this.getChrompackList();
    }, err => {
      //TODO exibir modal de erro
    });
  }

}
